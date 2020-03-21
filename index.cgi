#!/usr/bin/env ruby
# encoding: utf-8

require 'cgi'
require 'erb'
require 'httpclient'
require 'json'


@cgi = CGI.new
@client = HTTPClient.new
@title = "Bruschetta CGI"


def main
  if !@cgi["id"].empty?
    book_detail(@cgi["id"].to_i)
  elsif !(@cgi["title"].empty? && @cgi["author"].empty?)
    search(@cgi["title"], @cgi["author"])
  else
    page = @cgi["page"].empty? ? 1 : @cgi["page"].to_i
    index(page)
  end
end


def index(page)
  offset = 25 * (page - 1)
  json = @client.get("http://bruschetta/api/books/?limit=25&offset=#{offset.to_s}").body
  @books = JSON.parse(json)["books"]
  template = File.read("./views/index.erb")
  erb = ERB.new(template)

  print_header
  print erb.result
end


def search(title, author)
  query = {"title" => title, "author" => author}.delete_if{|k, v| v.empty? }.map{|k, v| k + "=" + v }.join("&")
  json = @client.get("http://bruschetta/api/search/?#{query}").body
  @books = JSON.parse(json)["books"]
  template = File.read("./views/index.erb")
  erb = ERB.new(template)

  print_header
  print erb.result
end


def book_detail(id)
  json = @client.get("http://bruschetta/api/book/#{id.to_s}/").body
  @book = JSON.parse(json)["books"][0]
  template = File.read("./views/detail.erb")
  erb = ERB.new(template)

  print_header
  print erb.result
end


def print_header
  print "content-type: text/html\n\n"
end


def title_with_vol(book)
  unless book["volume"].empty?
    "#{book["title"]} [#{book["volume"]}]"
  else
    book["title"]
  end
end



main
